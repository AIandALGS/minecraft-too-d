import random

from math import floor, ceil


class PerlinNoise:
    """Perlin noise is a type of gradient noise developed by Ken Perlin in
    1983. In our case, we will be using Perlin noise to generate heightmaps for
    one dimensional terrains, two dimensional terrains and three dimensional
    terrains.

    Author: https://rosettacode.org/wiki/Perlin_noise#Python

    Keywords:
    seed - the seed to be used for the Perlin noise generator.

    Attributes:
    p - a large permutation table.

    Function calls:
    set_permutation_table() - sets the permutation table.
    """

    p = [None] * 512

    def __init__(self, seed: int = 0) -> None:
        random.seed(seed)
        self.set_permutation_table()

    def __call__(self, x: int, y: int = 0, z: int = 0) -> int:
        """Upon calling the PerlinNoise class, generate a noise value for the
        passed x, y and z coordinate values. You can tweak the frequency,
        amplitude, and step settings for different terrain generation.

        Return the generated noise value for the passed x, y ad z coordinate
        values.

        Keywords:
        x - the passed x coordinate value.
        y - the passed y coordinate value, its default value is set to y = 0.
        z - the passed z coordinate value, its default value is set to z = 0.
        """

        frequency = 0.25
        amplitude = 5

        step = 0.05

        X = frequency * (x + step)
        Y = frequency * (y + step)
        Z = frequency * (z + step)

        return ceil(amplitude * self.generate_noise(X, Y, Z))

    def set_permutation_table(self) -> None:
        """Set the permutation table."""

        p = PerlinNoise.p

        permutation_table = [i for i in range(256)]
        random.shuffle(permutation_table)

        for j in range(256):
            p[256 + j] = p[j] = permutation_table[j]

        PerlinNoise.p = p

    def get_fade(self, t: float) -> float:
        """A smooth step function, in this case, is cubic curve.

        Return the value of f(t).

        Keywords:
        t - a function variable for f(t).
        """

        return t**3 * (t * (t * 6 - 15) + 10)

    def get_linear_interpolation(self, t: float, a: float, b: float) -> float:
        """Linear interpolation.

        Return the interpolated value.

        Keywords:
        t - a function variable for f(t).
        a - a function constant for f(t).
        b - a function constant for f(t).
        """

        return a + t * (b - a)

    def get_gradient(self, hash: int, x: int, y: int = 0, z: int = 0) -> float:
        """Convert the LO 4 bits of the hash code into 12 gradient directions.

        Return a unique gradient value for the given hash code and the passed
        x, y and z coordinate values.

        Keywords:
        hash - the passed hash code value.
        x - the passed x coordinate value.
        y - the passed y coordinate value, its default value is set to y = 0.
        z - the passed z coordinate value, its default value is set to z = 0.
        """

        h = hash & 15

        u = x if h < 8 else y
        v = y if h < 4 else (x if h in (12, 14) else z)

        return (u if (h & 1) == 0 else -u) + (v if (h & 2) == 0 else -v)

    def generate_noise(self, x: int, y: int = 0, z: int = 0) -> float:
        """Generate a noise value based on the passed x, y and z coordinate
        values.

        Return a noise value based on the passed x, y and z coordinate
        values.

        Keywords:
        x - the passed x coordinate value.
        y - the passed y coordinate value, its default value is set to y = 0.
        z - the passed z coordinate value, its default value is set to z = 0.
        """

        p = PerlinNoise.p

        X = floor(x) & 255
        Y = floor(y) & 255
        Z = floor(z) & 255

        # Relative X, Y, Z coordinates of point in cube
        x -= floor(x)
        y -= floor(y)
        z -= floor(z)

        # Compute the fade curves for each of the X, Y, Z coordinates
        u = self.get_fade(x)
        v = self.get_fade(y)
        w = self.get_fade(z)

        # Compute the hash coordinates
        A = p[X] + Y
        AA = p[A] + Z
        AB = p[A + 1] + Z
        B = p[X + 1] + Y
        BA = p[B] + Z
        BB = p[B + 1] + Z

        return self.get_linear_interpolation(
            w,
            self.get_linear_interpolation(
                v,
                self.get_linear_interpolation(
                    u,
                    self.get_gradient(p[AA], x, y, z),
                    self.get_gradient(p[BA], x - 1, y, z),
                ),
                self.get_linear_interpolation(
                    u,
                    self.get_gradient(p[AB], x, y - 1, z),
                    self.get_gradient(p[BB], x - 1, y - 1, z),
                ),
            ),
            self.get_linear_interpolation(
                v,
                self.get_linear_interpolation(
                    u,
                    self.get_gradient(p[AA + 1], x, y, z - 1),
                    self.get_gradient(p[BA + 1], x - 1, y, z - 1),
                ),
                self.get_linear_interpolation(
                    u,
                    self.get_gradient(p[AB + 1], x, y - 1, z - 1),
                    self.get_gradient(p[BB + 1], x - 1, y - 1, z - 1),
                ),
            ),
        )

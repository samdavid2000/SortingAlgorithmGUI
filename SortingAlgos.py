from graphics import update
from random import shuffle

"""
SortingAlgos

Class that has the purpose of showing the process of sorting
by every iteration with modifiable speed and various sorting algorithms,
this is shown on a Tkinter canvas with the purpose of being able to observe
each algorithm's behavior

It uses a Bars object to draw everything on a specified canvas, a data to be sorted and
a speed to slow the sorting process.

*Disclaimer*
Since we wanted to have a huge variety of algorithms, we based the ones used
with different resources such as GeekForGeeks articles and a Github Repository containing
such algorithms.

Links can be found here:
https://www.geeksforgeeks.org/python-program-for-bogosort-or-permutation-sort/
https://www.geeksforgeeks.org/odd-even-sort-brick-sort/
https://www.geeksforgeeks.org/python-program-for-quicksort/
https://www.geeksforgeeks.org/python-program-for-selection-sort/
https://www.geeksforgeeks.org/python-program-for-insertion-sort/
https://github.com/TheAlgorithms/Python/tree/master/sorts
"""


class SortingAlgos:
    # Constructor
    def __init__(self, bars, data, colors, speed):
        """[Constructor of SortingAlgos Class]

        Arguments:
            bars {[Bars]} -- [Bars that will be drawn and sorted]
            data {[List]} -- [List that will be represented and sorted]
            colors {[Tkinter Colors]} -- [Colors list for the color animations]
            speed {[Int]} -- [Speed in which the sorting will occur]
        """

        self.bars = bars
        self.data = data
        self.colors = colors
        self.speed = speed

    # Sorting Algorithms, visualized on Tkinter canvas using Bars
    def bubble_sort(self):
        """Bubble sort for python list
        """
        for _ in range(len(self.data) - 1):
            for j in range(len(self.data) - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    self.colors = ['red' if n == j or n == j + 1 else 'green' for n in range(len(self.data))]
                    self.bars.drawData(self.colors)
                    update(self.speed)
        self.colors = ['white' for n in range(len(self.data))]
        self.bars.drawData(self.colors)

    def insertion_sort(self):
        """Insertion sort for python list
        """
        for i in range(1, len(self.data)):
            key = self.data[i]
            j = i - 1
            while j >= 0 and key < self.data[j]:
                self.data[j + 1] = self.data[j]
                j -= 1
                self.colors = ['red' if n == j or n == j + 1 else 'green' for n in range(len(self.data))]
                self.bars.drawData(self.colors)
                update(self.speed)
            self.data[j + 1] = key
            self.colors = ['white' for n in range(len(self.data))]
            self.bars.drawData(self.colors)

    def selection_sort(self):
        """Selection sort for python list
        """
        for i in range(len(self.data)):
            min_idx = i
            for j in range(i + 1, len(self.data)):
                if self.data[min_idx] > self.data[j]:
                    min_idx = j

            self.data[i], self.data[min_idx] = self.data[min_idx], self.data[i]
            self.colors = ['red' if n == i or n == i + 1 else 'green' for n in range(len(self.data))]
            self.bars.drawData(self.colors)
            update(self.speed)

        self.colors = ['white' for n in range(len(self.data))]
        self.bars.drawData(self.colors)

    def even_odd_sort(self):
        """Even-Odd sort for python list
        """
        isSorted = 0
        while isSorted == 0:
            isSorted = 1
            temp = 0
            for i in range(1, len(self.data) - 1, 2):
                if self.data[i] > self.data[i + 1]:
                    self.data[i], self.data[i + 1] = self.data[i + 1], self.data[i]
                    self.colors = ['red' if n == i or n == i + 1 else 'green' for n in range(len(self.data))]
                    self.bars.drawData(self.colors)
                    update(self.speed)
                    isSorted = 0

            for i in range(0, len(self.data) - 1, 2):
                if self.data[i] > self.data[i + 1]:
                    self.data[i], self.data[i + 1] = self.data[i + 1], self.data[i]
                    self.colors = ['red' if n == i or n == i + 1 else 'green' for n in range(len(self.data))]
                    self.bars.drawData(self.colors)
                    update(self.speed)
                    isSorted = 0

        self.colors = ['white' for n in range(len(self.data))]
        self.bars.drawData(self.colors)

    def bogo_sort(self):
        """Bogo sort for python list
        """
        shuffle(self.data)
        self.colors = ['white' for n in range(len(self.data))]
        self.bars.drawData(self.colors)

        while self.data != sorted(self.data):
            shuffle(self.data)
            self.colors = ['white' for n in range(len(self.data))]
            self.bars.drawData(self.colors)
            update(self.speed)

        self.colors = ['white' for n in range(len(self.data))]
        self.bars.drawData(self.colors)

    def gnome_sort(self):
        """Gnome sort for python list
        """
        i = 1
        while i < len(self.data):
            if self.data[i - 1] <= self.data[i]:
                i += 1
            else:
                self.data[i - 1], self.data[i] = self.data[i], self.data[i - 1]
                self.colors = ['red' if n == i or n == i + 1 else 'green' for n in range(len(self.data))]
                self.bars.drawData(self.colors)
                update(self.speed)
                i -= 1
                if i == 0:
                    i = 1

        self.colors = ['white' for n in range(len(self.data))]
        self.bars.drawData(self.colors)

    def pancake_sort(self):
        """Pancake sort for python list
        """
        cur = len(self.data)
        while cur > 1:
            mi = self.data.index(max(self.data[0:cur]))

            self.data = self.data[mi::-1] + self.data[mi + 1: len(self.data)]

            self.data = self.data[cur - 1:: -1] + self.data[cur: len(self.data)]
            cur -= 1

        self.colors = ['white' for n in range(len(self.data))]
        self.bars.drawData(self.colors)

    def cycle_sort(self):
        """Cycle sort for python list
        """
        ans = 0

        for cycleStart in range(0, len(self.data) - 1):
            item = self.data[cycleStart]

            pos = cycleStart
            for i in range(cycleStart + 1, len(self.data)):
                if self.data[i] < item:
                    pos += 1

            if pos == cycleStart:
                continue

            while item == self.data[pos]:
                pos += 1
            self.data[pos], item = item, self.data[pos]
            self.colors = ['red' if n == pos or n == pos + 1 else 'green' for n in range(len(self.data))]
            self.bars.drawData(self.colors)
            update(self.speed)
            ans += 1

            while pos != cycleStart:

                pos = cycleStart
                for i in range(cycleStart + 1, len(self.data)):
                    if self.data[i] < item:
                        pos += 1

                while item == self.data[pos]:
                    pos += 1
                self.data[pos], item = item, self.data[pos]

                self.colors = ['red' if n == pos or n == pos + 1 else 'green' for n in range(len(self.data))]
                self.bars.drawData(self.colors)
                update(self.speed)
                ans += 1

        self.colors = ['white' for n in range(len(self.data))]
        self.bars.drawData(self.colors)

    def shell_sort(self):
        """Shell sort for python list
        """
        gaps = [701, 301, 132, 57, 23, 10, 4, 1]

        for gap in gaps:
            i = gap
            while i < len(self.data):
                temp = self.data[i]
                j = i
                while j >= gap and self.data[j - gap] > temp:
                    self.data[j] = self.data[j - gap]
                    self.colors = ['red' if n == j or n == j + 1 else 'green' for n in range(len(self.data))]
                    self.bars.drawData(self.colors)
                    update(self.speed)
                    j -= gap
                self.data[j] = temp
                self.colors = ['red' if n == j or n == j + 1 else 'green' for n in range(len(self.data))]
                self.bars.drawData(self.colors)
                update(self.speed)
                i += 1
        self.colors = ['white' for n in range(len(self.data))]
        self.bars.drawData(self.colors)

    def cocktail_shaker_sort(self):
        """Cocktail shaker sort for python list
        """
        for i in range(len(self.data) - 1, 0, -1):
            swapped = False

            for j in range(i, 0, -1):
                if self.data[j] < self.data[j - 1]:
                    self.data[j], self.data[j - 1] = self.data[j - 1], self.data[j]
                    self.colors = ['red' if n == j or n == j + 1 else 'green' for n in range(len(self.data))]
                    self.bars.drawData(self.colors)
                    update(self.speed)
                    swapped = True

            for j in range(i):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    self.colors = ['red' if n == j or n == j + 1 else 'green' for n in range(len(self.data))]
                    self.bars.drawData(self.colors)
                    update(self.speed)
                    swapped = True

            if not swapped:
                self.colors = ['white' for n in range(len(self.data))]
                self.bars.drawData(self.colors)

    def comb_sort(self):
        """Comb sort for python list
        """
        shrink_factor = 1.3
        gap = len(self.data)
        completed = False

        while not completed:
            gap = int(gap / shrink_factor)
            if gap <= 1:
                completed = True

            index = 0
            while index + gap < len(self.data):
                if self.data[index] > self.data[index + gap]:
                    self.data[index], self.data[index + gap] = self.data[index + gap], self.data[index]
                    self.colors = ['red' if n == index or n == index + 1 else 'green' for n in range(len(self.data))]
                    self.bars.drawData(self.colors)
                    update(self.speed)
                    completed = False
                index += 1

        self.colors = ['white' for n in range(len(self.data))]
        self.bars.drawData(self.colors)

    def pigeon_sort(self):
        """Pigeon sort for python list
        """
        min = self.data[0]
        max = self.data[0]

        for i in range(len(self.data)):
            if self.data[i] < min:
                min = self.data[i]
            elif self.data[i] > max:
                max = self.data[i]

        holes_range = max - min + 1
        holes = [0 for _ in range(holes_range)]
        holes_repeat = [0 for _ in range(holes_range)]

        for i in range(len(self.data)):
            index = self.data[i] - min
            if holes[index] != self.data[i]:
                holes[index] = self.data[i]
                holes_repeat[index] += 1
            else:
                holes_repeat[index] += 1

        index = 0
        for i in range(holes_range):
            while holes_repeat[i] > 0:
                self.data[index] = holes[i]
                self.colors = ['red' if n == index or n == index + 1 else 'green' for n in range(len(self.data))]
                self.bars.drawData(self.colors)
                update(self.speed)
                index += 1
                holes_repeat[i] -= 1

        self.colors = ['white' for n in range(len(self.data))]
        self.bars.drawData(self.colors)







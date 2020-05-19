from tkinter import *

class InfoWin:
    def __init__(self, sort_option):
        '''Creates a window object to be called in the GUI class'''
        top = Tk() #root
        top.iconbitmap('icon.ico')
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        #The window itself
        top.geometry("656x786+908+97")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("Algorithm Info")
        top.configure(background="#34495E", highlightbackground="#d9d9d9", highlightcolor="black")

        #Inner black frame
        self.Canvas1 = Canvas(top)
        self.Canvas1.place(relx=0.056, rely=0.038, relheight=0.92, relwidth=0.887)
        self.Canvas1.configure(background="#1a1a1a", borderwidth="2", highlightbackground="#d9d9d9", highlightcolor="black", insertbackground="black", relief="ridge", selectbackground="#c4c4c4", selectforeground="black")
        
        #Title with Sorting Algorithm
        self.Title = Message(self.Canvas1)
        self.Title.place(relx=0.25, rely=0.043, relheight=0.058, relwidth=0.45, anchor = N)
        self.Title.configure(background="#1a1a1a", font="-family {Segoe UI} -size 20 -weight bold", foreground="#ffffff", highlightbackground="#d9d9d9", highlightcolor="black", width=400)

        #Message with Properties
        self.Properties = Message(self.Canvas1)
        self.Properties.place(relx=0.25, rely=0.124, relheight=0.188, relwidth=0.45, anchor = N)
        self.Properties.configure(background="#1a1a1a", font="-family {Segoe UI} -size 10", foreground="#ffffff", highlightbackground="#d9d9d9", highlightcolor="black", width=282)

        #Body Message with information
        self.Body = Message(self.Canvas1)
        self.Body.place(relx=0.5, rely=0.335, relheight=0.611, relwidth=0.900, anchor = N)
        self.Body.configure(background="#212121", font="-family {Segoe UI} -size 10", foreground="#ffffff", highlightbackground="#d9d9d9", highlightcolor="black", width=500)

        #Method that changes the information text depending on the sorting algorithm
        self.setText(sort_option)

        top.mainloop()
    
    def setText(self, sort_option):
        '''Method that sets the text of the canvas' components, depending on the chosen sorting algorithm'''
        if sort_option == 'Bubble Sort':
            #BUBBLE SORT
            self.Title.configure(text='''BUBBLE SORT''')
            self.Properties.configure(text='''Properties:
 Stable
 In-place
 O(n2) comparisons and swaps
 Not online
 Adaptive: O(n) when nearly sorted''')
            self.Body.configure(text='''Sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted. The algorithm, which is a comparison sort, is named for the way smaller elements "bubble" to the top of the list. Although the algorithm is simple, it is too slow and impractical for most problems even when compared to insertion sort. It can be practical if the input is usually in sorted order but may occasionally have some out-of-order elements nearly in position.

The bubble sort algorithm can be easily optimized by observing that the nth pass finds the nth largest element and puts it into its final place. So, the inner loop can avoid looking at the last n-1 items when running for the nth time.

Algorithm:
for i = 1:n,
    swapped = false
    for j = n:i + 1,
        if a[j] < a[j - 1],
            swap a[j, j - 1]
            swapped = true
    break if not swapped
end''')
        elif sort_option == 'Insertion Sort':
            #INSERTION SORT
            self.Title.configure(text='''INSERTION SORT''')
            self.Properties.configure(text='''Properties:
 Stable
 In-place
 O(n2) comparisons and swaps
 Online
 Adaptive: O(n) when nearly sorted
 Very less overhead''')
            self.Body.configure(text='''It is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. However, insertion sort provides several advantages such as Simple implementation, efficient for (quite) small data sets, more efficient in practice than most other simple quadratic (i.e., O(n2)) algorithms such as selection sort or bubble sort and usually faster in practice than asymptotically faster algorithms for small data sets.

Algorithm:
for i = 2:n,
    for (k = i; k > 1 and a[k] < a[k - 1]; k--)
        swap a[k], a[k - 1]
end''')
        elif sort_option == 'Selection Sort':
            #SELECTION SORT
            self.Title.configure(text='''SELECTION SORT''')
            self.Properties.configure(text='''Properties:
 Not Stable
 O(1) extra space
 O(n2) comparisons
 O(n) swaps
 Not Adaptive''')
            self.Body.configure(text='''Selection Sort is best when swapping items is very costly.
It is an in-place comparison sorting algorithm. It has an O(n2) time complexity, which makes it inefficient on large lists, and generally performs worse than the similar insertion sort. Selection sort is noted for its simplicity and has performance advantages over more complicated algorithms in certain situations, particularly where auxiliary memory is limited. The algorithm divides the input list into two parts: a sorted sublist of items which is built up from left to right at the front (left) of the list and a sublist of the remaining unsorted items that occupy the rest of the list. Initially, the sorted sublist is empty and the unsorted sublist is the entire input list. The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, exchanging (swapping) it with the leftmost unsorted element (putting it in sorted order), and moving the sublist boundaries one element to the right. The time efficiency of selection sort is quadratic, so there are a number of sorting techniques which have better time complexity than selection sort. One thing which distinguishes selection sort from other sorting algorithms is that it makes the minimum possible number of swaps, n − 1 in the worst case.

Algorithm Pseudocode:
    Find the smallest card. Swap it with the first card.
    Find the second-smallest card. Swap it with the second card.
    Find the third-smallest card. Swap it with the third card.
    Repeat finding the next-smallest card, and swapping it into the correct position until the array is sorted''')
        elif sort_option == 'Even-Odd Sort':
            #SELECTION SORT
            self.Title.configure(text='''EVEN-ODD SORT''')
            self.Properties.configure(text='''Properties:
 Stable
 Worst-case performance O(n2)
 Best-case performance O(n)
 Worst-case space complexity O(1)''')
            self.Body.configure(text='''It is a relatively simple sorting algorithm, developed originally for use on parallel processors with local interconnections. It is a comparison sort related to bubble sort, with which it shares many characteristics. It functions by comparing all odd/even indexed pairs of adjacent elements in the list and, if a pair is in the wrong order (the first is larger than the second) the elements are switched. The next step repeats this for even/odd indexed pairs (of adjacent elements). Then it alternates between odd/even and even/odd steps until the list is sorted.

Odd phase: Every odd indexed element is compared with the next even indexed element(considering 1-based indexing).
Even phase: Every even indexed element is compared with the next odd indexed element.

Algorithm Pseudocode:
id = process's label 	
for i = 1 to n do 	
    if i is odd and id is odd then 
        compare-exchange_min(id + 1); 
    else
        compare-exchange_max(id - 1);
         
    if i is even and id is even then 
        compare-exchange_min(id + 1); 
    else 
        compare-exchange_max(id - 1);			
end for''')
        elif sort_option == 'Bogo Sort':
            #BOGO SORT
            self.Title.configure(text='''BOGO SORT''')
            self.Properties.configure(text='''Properties:
 Not Stable
 Worst complexity: Infinite
 Average complexity: n*n!
 Best complexity: n
 Space complexity: 1
 Worst-case space complexity: O(n)''')
            self.Body.configure(text='''It is a highly inefficient sorting algorithm based on the generate and test paradigm. The function successively generates permutations of its input until it finds one that is sorted. It is not useful for sorting, but may be used for educational purposes, to contrast it with more efficient algorithms. Two versions of this algorithm exist: a deterministic version that enumerates all permutations until it hits a sorted one, and a randomized version that randomly permutes its input. An analogy for the working of the latter version is to sort a deck of cards by throwing the deck into the air, picking the cards up at random, and repeating the process until the deck is sorted. Its name is a portmanteau of the words bogus and sort.

Algorithm Pseudocode:
import random

def is_sorted(data) -> bool:
    """Determine whether the data is sorted."""
    return all(data[i] <= data[i+1] for i in range(len(data)-1))

def bogosort(data) -> list:
    """Shuffle data until sorted."""
    while not is_sorted(data):
        random.shuffle(data)
    return data''')
        elif sort_option == 'Gnome Sort':
            #GNOME SORT
            self.Title.configure(text='''GNOME SORT''')
            self.Properties.configure(text='''Properties:
 Stable
 Worst complexity: O(n2)
 Average complexity: O(n2)
 Best complexity: O(n)
 Space complexity: O(1)''')
            self.Body.configure(text='''It is a sorting algorithm which is similar to insertion sort in that it works with one item at a time but gets the item to the proper place by a series of swaps, similar to a bubble sort. It is conceptually simple, requiring no nested loops. The average running time is O(n2) but tends towards O(n) if the list is initially almost sorted. The algorithm finds the first place where two adjacent elements are in the wrong order and swaps them. It takes advantage of the fact that performing a swap can introduce a new out-of-order adjacent pair next to the previously swapped elements. It does not assume that elements forward of the current position are sorted, so it only needs to check the position directly previous to the swapped elements.

Algorithm Pseudocode:
procedure gnomeSort(a[]):
    pos := 0
    while pos < length(a):
        if (pos == 0 or a[pos] >= a[pos-1]):
            pos := pos + 1
        else:
            swap a[pos] and a[pos-1]
            pos := pos - 1''')
        elif sort_option == 'Cycle Sort':
            #CYCLE SORT
            self.Title.configure(text='''CYCLE SORT''')
            self.Properties.configure(text='''Properties:
 Not Stable
 Worst complexity: O(n2)
 Average complexity: O(n2)
 Best complexity: O(n2)
 Space complexity: O(1)''')
            self.Body.configure(text='''It is an in-place, unstable sorting algorithm, a comparison sort that is theoretically optimal in terms of the total number of writes to the original array, unlike any other in-place sorting algorithm. It is based on the idea that the permutation to be sorted can be factored into cycles, which can individually be rotated to give a sorted result. Unlike nearly every other sort, items are never written elsewhere in the array simply to push them out of the way of the action. Each value is either written zero times, if it's already in its correct position, or written one time to its correct position. This matches the minimal number of overwrites required for a completed in-place sort. Minimizing the number of writes is useful when making writes to some huge data set is very expensive, such as with EEPROMs like Flash memory where each write reduces the lifespan of the memory.

Algorithm:
1. If the element is already at the correct position, do nothing.
2. If it is not, we will write it to its intended position. That position is inhabited by a different element b, which we then have to move to its correct position. This process of displacing elements to their correct positions continues until an element is moved to the original position of a. This completes a cycle.''')
        elif sort_option == 'Shell Sort':
            #SHELL SORT
            self.Title.configure(text='''SHELL SORT''')
            self.Properties.configure(text='''Properties:
 Not Stable
 In-place
 Complexity depends upon gap
 Not online
 Adaptive: O(n.log(n)) when nearly sorted''')
            self.Body.configure(text='''It can be seen as either a generalization of sorting by exchange (bubble sort) or sorting by insertion (insertion sort). The worse-case time complexity of shell sort depends on the increment sequence. The method starts by sorting pairs of elements far apart from each other, then progressively reducing the gap between elements to be compared. Starting with far apart elements can move some out-of-place elements into position faster than a simple nearest neighbor exchange.

Algorithm Pseudocode:
gaps = [x, y, z, …]
for each (G in gaps)
    create sub-arrays with elements having gap as G
    for each(S in sub-arrays)
        insertion_sort(s)
    merge all sub-arrays''')
        elif sort_option == 'Cocktail Shaker Sort':
            #COCKTAIL SHAKER SORT
            self.Title.configure(text='''Cocktail Shaker Sort''')
            self.Properties.configure(text='''Properties:
 Stable
 Worst complexity: O(n2)
 Average complexity: O(n2)
 Best complexity: O(n)
 Space complexity: O(1)''')
            self.Body.configure(text='''It is an extension of bubble sort. The algorithm extends bubble sort by operating in two directions. While it improves on bubble sort by more quickly moving items to the beginning of the list, it provides only marginal performance improvements. Like most variants of bubble sort, cocktail shaker sort is used primarily as an educational tool. More performant algorithms such as timsort, or merge sort are used by the sorting libraries built into popular programming languages such as Python and Java.

Algorithm Pseudocode:
procedure cocktailShakerSort(A : list of sortable items) is
    do
        swapped := false
        for each i in 0 to length(A) − 2 do:
            if A[i] > A[i + 1] then // test whether the two elements are in the wrong order
                swap(A[i], A[i + 1]) // let the two elements change places
                swapped := true
        if not swapped then
            // we can exit the outer loop here if no swaps occurred.
            break do-while loop
        swapped := false
        for each i in length(A) − 2 to 0 do:
            if A[i] > A[i + 1] then
                swap(A[i], A[i + 1])
                swapped := true
    while swapped // if no elements have been swapped, then the list is sorted
end procedure''')
        elif sort_option == 'Comb Sort':
            #COMB SORT
            self.Title.configure(text='''COMB SORT''')
            self.Properties.configure(text='''Properties:
 Not Stable
 Worst complexity: n^2
 Average complexity: n*log(n)
 Best complexity: n
 Space complexity: 1''')
            self.Body.configure(text='''It improves on Bubble Sort. In bubble sort, when any two elements are compared, they always have a gap (distance from each other) of 1. The basic idea of comb sort is that the gap can be much more than 1.

Algorithm Pseudocode:

function combsort(array input) is
    gap := input.size                    // Initialize gap size
    shrink := 1.3 // Set the gap shrink factor
    sorted := false 
    loop while sorted = false
                                        // Update the gap value for a next comb
        gap := floor(gap / shrink)
        if gap ≤ 1 then
            gap := 1
            sorted := true              // If there are no swaps this pass, we are done
                                        // A single "comb" over the input list
        i := 0
        loop while i + gap < input.size // See Shell sort for a similar idea
            if input[i] > input[i+gap] then
                swap(input[i], input[i+gap])
                sorted := false
                                        // If this assignment never happens within the loop,
                                        // then there have been no swaps and the list is sorted.
             i := i + 1''')
        elif sort_option == 'Pigeon Sort':
            #PIGEON SORT
            self.Title.configure(text='''PIGEON SORT''')
            self.Properties.configure(text='''Properties:
 Stable
 Worst complexity: n+2^k
 Average complexity: n+2^k
 Space complexity: 2^k
 Worst-case performance: where N is the range of key values and n is the input size''')
            self.Body.configure(text='''It is a sorting algorithm that is suitable for sorting lists of elements where the number of elements (n) and the length of the range of possible key values (N) are approximately the same. It requires O(n + N) time. It is similar to counting sort, but differs in that it "moves items twice: once to the bucket array and again to the final destination [whereas] counting sort builds an auxiliary array then uses the array to compute each item's final destination and move the item there."

Algorithm:
1. Given an array of values to be sorted, set up an auxiliary array of initially empty "pigeonholes," one pigeonhole for each key through the range of the original array.

2. Going over the original array, put each value into the pigeonhole corresponding to its key, such that each pigeonhole eventually contains a list of all values with that key.

3. Iterate over the pigeonhole array in order, and put elements from non-empty pigeonholes back into the original array.''')




class quickSort {
    public static void sorted(int[] a, int low, int high) {
        if (low < high) {
            int partIndex = partition(a, low, high);
            sorted(a, low, partIndex - 1);
            sorted(a, partIndex + 1, high);
        }
    }

    static int partition(int[] a, int low, int high) {
        int i = low;
        int j = high;
        int pivot = a[low];

        while (i < j) {
            while (a[i] <= pivot && i <= high - 1) {
                i++;
            }
            while (a[j] > pivot && j >= low + 1) {
                j--;
            }
            if (i < j) {
                int temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
        int t = a[low];
        a[low] = a[j];
        a[j] = t;
        return j;
    }

    public static void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }

    public static void main(String[] args) {
        int[] a = {12, 43, 53, 121, 6, 2, 3};
        sorted(a, 0, a.length - 1);
        printArray(a);
    }
}


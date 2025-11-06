class Solution {
    public int[] processQueries(int n, int[][] connections, int[][] queries) {
        n++;
        final int[] l = new int[n];
        for (int i = 1; i < n; i++) {
            l[i] = i;
        }
        for (int[] as : connections) {
            l[getLabel(l, as[0])] = l[getLabel(l, as[1])];
        }
        final int[] counts = new int[n];
        for (int i = 0; i < n; i++) {
            counts[getLabel(l, i)]++;
        }
        updateCounts(counts);
        final int[] starts = counts.clone();
        final int[] sorted = new int[n];
        for (int i = 0; i < n; i++) {
            sorted[counts[l[i]]++] = i;
        }
        final int[] r = new int[queries.length];
        int len = 0;
        final boolean[] offline = new boolean[n];
        for (var q: queries) {
            final int x = q[1];
            if (q[0] == 1) {
                if (offline[x]) {
                    final int label = l[x];
                    final int end = counts[label];
                    int start = starts[label];
                    while (start < end && offline[sorted[start]]) {
                        start++;
                    }
                    starts[label] = start;
                    r[len++] = start == end ? -1 : sorted[start];
                } else {
                    r[len++] = x;
                }
            } else {
                offline[x] = true;
            }
        }
        return Arrays.copyOf(r, len);
    }


    static final int[] arr = new int[100_001];

    private static int check(int[] sorted, int[] source, int[] target, int start, int end) {
        int r = 0;
        for (int i = start; i < end; i++) {
            final int idx = sorted[i];
            if (++arr[source[idx]] > 0) r++;
            if (arr[target[idx]]-- > 0) r--;
        }
        for (int i = start; i < end; i++) {
            final int idx = sorted[i];
            arr[source[idx]] = 0;
            arr[target[idx]] = 0;
        }
        return r;
    }

    private static void updateCounts(int[] count) {
        int sum = 0;
        for (int r = 0; r < count.length; r++) {
            final int newSum = sum + count[r];
            count[r] = sum;
            sum = newSum;
        }
    }

    static int getLabel(final int[] labels, int idx) {
        final int current = labels[idx];
        return (current == idx || current < 0)? idx : (labels[idx] = getLabel(labels, current));
    }
}

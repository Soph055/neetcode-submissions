public class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // map: number -> how many times it appears in nums
        Map<Integer, Integer> count = new HashMap<>();

        // buckets indexed by frequency: freq[i] = list of numbers that appear exactly i times
        // size is nums.length + 1 because max possible frequency = nums.length (all elements identical)
        List<Integer>[] freq = new List[nums.length + 1];
        for (int i = 0; i < freq.length; i++) {
            freq[i] = new ArrayList<>(); // init every bucket so we can safely .add() later
        }

        // count occurrences of each number
        for (int n : nums) {
            count.put(n, count.getOrDefault(n, 0) + 1); // getOrDefault avoids NPE on first sighting
        }

        // drop each number into the bucket matching its frequency
        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            freq[entry.getValue()].add(entry.getKey()); // getValue() = frequency (index), getKey() = the number
        }

        // walk buckets from highest frequency down to lowest, collecting until we have k numbers
        int[] res = new int[k];
        int index = 0;
        for (int i = nums.length; i > 0; i--) { // start at max possible frequency, go down to 1
            for (int n : freq[i]) {
                res[index++] = n; // place number, then advance pointer
                if (index == k) {
                    return res; // k results found — exit immediately, no need to check outer loop condition
                }
            }
        }

        return res; // unreachable in practice since k is always <= number of unique elements, but keeps compiler happy
    }
}
//Runtime: 0 ms, faster than 100.00% of Java online submissions for Binary Search.
// Memory Usage: 39.9 MB, less than 69.43% of Java online submissions for Binary Search.

class Solution {
    public int search(int[] arr, int target) {
        int start = 0;
        int end = arr.length -1;
        int mid = start + (end-start)/2;
        while (start<=end){
            mid = start + (end-start)/2;
             if (arr[mid] == target ){
                    return mid;
                }
                if(target<arr[mid]){
                    end = mid-1;
                }else  {
                    start = mid+1;
                }
        }
        return -1;
    }
   
}

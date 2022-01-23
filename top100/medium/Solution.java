package medium;

import java.util.Arrays;

// this Solution.java is for 31_NextPermutation problem
// used to debug my python code

public class Solution {
  public static void nextPermutation(int[] nums) {
      int i = nums.length - 2;
      while (i >= 0 && nums[i + 1] <= nums[i]) {
          i--;
      }
      if (i >= 0) {
          int j = nums.length - 1;
          while (nums[j] <= nums[i]) {
              j--;
          }
          swap(nums, i, j);
          System.out.print("after swapping " + i + "th and " + j + "th: ");
          System.out.println(Arrays.toString(nums));
      }
      reverse(nums, i + 1);
  }

  private static void reverse(int[] nums, int start) {
      int i = start, j = nums.length - 1;
      while (i < j) {
          swap(nums, i, j);
          i++;
          j--;
          System.out.println("reverse: i = " + i + ", j = " + j);
          System.out.println("array = " + Arrays.toString(nums));
      }
  }

  private static void swap(int[] nums, int i, int j) {
      int temp = nums[i];
      nums[i] = nums[j];
      nums[j] = temp;
  }

  public static void main(String args[]){
    int[] array = {2, 1, 2, 2, 2, 2, 2, 1};
    System.out.println("initial array: "+ Arrays.toString(array));
    nextPermutation(array);
    System.out.println("next permutation: " + Arrays.toString(array));
  }
}

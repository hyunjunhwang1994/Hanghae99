import java.util.HashSet;

public class q34 {
    public static void main(String[] args) {

    }


    public static int solution(int[] nums){
        int max = nums.length / 2;

        // 중복제거하기
        HashSet<Integer> numsSet = new HashSet<>();

        for (int num : nums) {
            numsSet.add(num);
        }

        // 중복을 제거한 셋의 크기가 max보다 크면 max를, 작으면 numsSet의 size를 리턴
        if (numsSet.size() > max) {
            return max;
        } else {
            return numsSet.size();
        }
    }

}

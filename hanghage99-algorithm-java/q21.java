public class q21 {

    public static void main(String[] args) {

    }


    public static int solution(int[] nums){
        int answer = 0;


        for(int i = 0; i<nums.length; i++){
            for(int j = i + 1; j < nums.length; j++){
                for(int k = j + 1; k < nums.length; k++){

                    int sum = nums[i] + nums[j] + nums[k];


                    answer += isPrime(sum) ? 1 : 0;

                }

            }

        }

        return answer;

    }


    public static boolean isPrime(int num){

        for(int i = 2; i<= Math.sqrt(num); i++){

            if(num % i == 0){
                return false;
            }

        }
        return true;

    }




}

public class q7 {

    public static void main(String[] args) {


        long n = 12412412412224L;

        for (int ar : solution(n)){
            System.out.printf("["+ar+"]");
        }


        }



    public static int[] solution(long n) {

        int length = (int)(Math.log10(n)+1);
        int[] answer = new int[length];


        for(int i=0; i<length; i++){
            answer[i] = (int)(n % 10);
            n /= 10;
        }


        return answer;


    }
}

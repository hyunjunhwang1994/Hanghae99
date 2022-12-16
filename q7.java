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

//        // 자릿수 Math 함수 없이 구하기
//        int cnt = 0;
//        while (n != 0){
//            n /= 10;
//            cnt ++;
//        }


        for(int i=0; i<length; i++){
            answer[i] = (int)(n % 10);
            n /= 10;
        }


        return answer;


    }
}

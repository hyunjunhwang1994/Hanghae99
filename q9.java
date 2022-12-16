public class q9 {




    public static void main(String[] args) {

        System.out.println(solution(9));




    }

    public static long solution(long n) {
        Double sqrt = Math.sqrt(n);

        if(sqrt == sqrt.intValue()){
            return (long)Math.pow(sqrt + 1, 2);
        } else return -1;
    }



}

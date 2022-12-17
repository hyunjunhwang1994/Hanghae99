import java.util.Arrays;

public class q20 {
    public static void main(String[] args) {


        System.out.println(solution("qwdokDsSaXXzwDklqwC"));




    }


    public static String solution(String s){
        char[] arr = s.toCharArray();
        Arrays.sort(arr);
        return new StringBuilder(new String(arr)).reverse().toString();
    }


}

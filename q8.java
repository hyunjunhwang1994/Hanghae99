import java.util.Arrays;

public class q8 {

    public static void main(String[] args) {

        solution(124124);

    }




    public static long solution(long n){

        String[] list = String.valueOf(n).split("");
        Arrays.sort(list);

        StringBuilder sb = new StringBuilder();
        for (String aList : list) sb.append(aList);

        return Long.parseLong(sb.reverse().toString());


    }




}

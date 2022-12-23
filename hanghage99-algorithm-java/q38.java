public class q38 {
    public static void main(String[] args) {


        solution("1 2 3 4");
    }

    public static String solution(String s) {

        String[] tmp = s.split(" ");


        for (String s1 : tmp) {
            System.out.println(s1);
        }
        
        int min, max, n;
        min = max = Integer.parseInt(tmp[0]);
        for (int i = 1; i < tmp.length; i++) {
            n = Integer.parseInt(tmp[i]);
            if(min > n) min = n;
            if(max < n) max = n;
        }

        return min + " " + max;
    }
}

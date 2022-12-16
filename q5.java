public class q5 {

    public static void main(String[] args) {

        System.out.println(solution("abdefsfsff sdqsd sada"));
    }




    public static String solution(String s){

        String answer = "";
        int cnt = 0;


        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);

            if(c == ' '){
                answer += " ";
                cnt = 0;
                continue;
            }

            if((cnt % 2) == 0){
                answer += String.valueOf(Character.toUpperCase(c));
                cnt++;
            }else{
                answer += String.valueOf(Character.toLowerCase(c));
                cnt++;
            }
        }
        return answer;

    }


}

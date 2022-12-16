public class q3_subak {
    public static void main(String[] args) {


        System.out.println(solution(21));


    }


    public static String solution(int n){
        String answer = "";
        int cnt = 0;
        String words1 ="수";
        String words2 ="박";

        for(int i = 1; i <= n; i++){
            if(cnt == 0){
                answer += words1;
                cnt = 1;
            }else{
                answer += words2;
                cnt = 0;
            }
        }




        return answer;

    }

}

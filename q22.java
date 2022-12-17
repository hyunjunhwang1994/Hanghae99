import java.util.ArrayList;

public class q22 {

    public static void main(String[] args) {


        System.out.println(solution("one4seveneight"));
    }


    public static int solution(String s){
        int answer = 0;
        String temp = s;
        // 1. 입력 : "one4seveneight"
        // 2. 스트링중 one, seven, eight.. 찾아라.
        // 4는 그대로 표시이므로 놔두고,
        // 3. 찾은 것들을 1,  (4) 7, 8로 바꿔라.
        String [] sList = {
                "zero","one","two","three","four","five","six","seven","eight","nine"
        };
        String [] iList ={
                "0","1","2","3","4","5","6","7","8","9"
        };

        for(int i = 0; i < sList.length; i++){

            if(s.indexOf(sList[i]) >= 0){
                temp = temp.replace(sList[i],iList[i]);
            }

        }

        answer = Integer.parseInt(temp);

        return answer;
    }
}

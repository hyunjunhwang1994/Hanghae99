import java.util.ArrayList;

public class q15 {


    public static void main(String[] args) {



    }


    public static int[] solution(int []arr){

        ArrayList<Integer> tempList = new ArrayList<Integer>();

        int preNum = 10;

        for(int num : arr) {

            if(preNum != num)
                tempList.add(num);

            preNum = num;

        }

        int[] answer = new int[tempList.size()];

        for(int i=0; i<answer.length; i++) {
            answer[i] = tempList.get(i).intValue();
        }
        return answer;
    }



}

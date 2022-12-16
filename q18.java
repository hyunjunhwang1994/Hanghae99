import java.util.ArrayList;
import java.util.List;

public class q18 {

    public static void main(String[] args) {


    }


    public static int[] solution(int[] answers){
        int[] supo1 = {1,2,3,4,5};
        int[] supo2 = {2,1,2,3,2,4,2,5};
        int[] supo3 = {3,3,1,1,2,2,4,4,5,5};

        int[] count = new int[3];


        for(int i = 0; i<answers.length;i++){
            if(answers[i] == supo1[i%5]) count[0]++;
            if(answers[i] == supo2[i%8]) count[1]++;
            if(answers[i] == supo3[i%10]) count[2]++;

        }

        int max = Math.max(count[0], Math.max(count[1], count[2]));

        List<Integer> list = new ArrayList<>();

        if(max == count[0])
            list.add(1);
        if(max == count[1])
            list.add(2);
        if(max == count[2])
            list.add(3);

        int[] answer = new int[list.size()];
        for(int i=0; i<list.size(); i++){
            answer[i] = list.get(i);
        }

        return answer;



    }
}

import java.util.Arrays;

public class q4 {


    public static void main(String[] args) {

        String[] participant = {"mislav", "stanko", "mislav", "ana"};
        String[] completion = {"stanko", "ana", "mislav"};
        System.out.println(solution(participant,completion));

    }


    public static String solution(String[] participant, String[] completion){

        Arrays.sort(participant);
        Arrays.sort(completion);

        for(String s : participant){
            System.out.println(s);
        }
        for(String s : completion){
            System.out.println(s);
        }



        for(int i = 0; i < completion.length; i++){


            if(participant[i].equals(completion[i])){
                continue;
            }else{
                return participant[i];
            }

        }
        return participant[participant.length-1];

    }








}

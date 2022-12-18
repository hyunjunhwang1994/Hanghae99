import java.util.Arrays;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

public class q4 {


    public static void main(String[] args) {
        String[] participant = {"mislav", "stanko", "mislav", "ana"};
        String[] completion = {"stanko", "ana", "mislav"};
        System.out.println(solution(participant,completion));

    }

//    public static String solution(String[] participant, String[] completion){
//
//        Arrays.sort(participant);
//        Arrays.sort(completion);
//
//        for(int i = 0; i < completion.length; i++){
//
//            if(participant[i].equals(completion[i])){
//                continue;
//            }else{
//                return participant[i];
//            }
//        }
//        return participant[participant.length-1];
//
//    }

        public static String solution(String[] participant, String[] completion){

            String answer ="";

            HashMap<String, Integer> map = new HashMap<>();

            for(String p : participant)
                map.put(p, map.getOrDefault(p,0) + 1);
            for(String c : completion)
                map.put(c, map.get(c) - 1 );

            Iterator<Map.Entry<String, Integer>> iter = map.entrySet().iterator();

            while (iter.hasNext()){
                Map.Entry<String, Integer> entry = iter.next();
                if(entry.getValue() != 0){
                    answer = entry.getKey();
                    break;
                }
            }

        return answer;

    }






}

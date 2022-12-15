public class MemberService {





    boolean login(String id, String password){
        boolean result;

        if(id.equals("hong") && password.equals("12345")){
            result = true;
        }else{
            result= false;
        }
        return  result;
    }

    void logout(String id){
        System.out.println("로그아웃 되었습니다.");

    }


}

package sec08.quiz.$2;

public class MySql implements DataAccessObject{

    @Override
    public void select() {
        System.out.println("MySql DB에서 검색");

    }

    @Override
    public void insert() {
        System.out.println("MySql DB에서 십입");
    }

    @Override
    public void update() {
        System.out.println("MySql DB에서 수정");
    }

    @Override
    public void delete() {
        System.out.println("MySql DB에서 삭제");
    }
}

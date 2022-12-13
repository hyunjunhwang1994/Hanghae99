


$(document).ready(function() {

    $("#openPop").click(function() {
        $("#banner_online").show();
    });

    $("#openModalPop").click(function() {
        $("#banner_online").fadeIn();
        $("#modal").fadeIn();
    });

    $("#close_button").click(function(){
        $("#banner_online").fadeOut();
        $("#modal").fadeOut();
    });
});


        function showFriend(user_id) {
            $.ajax({
                type: "POST",
                url: "/api/showfriend",
                data: {},
                success: function (response) {

                    $('#showFriend').empty()

                    let rows = response
                    let temp_heml = ``
                    let userId = user_id
                    for (let i = 0; i < rows.length; i++) {
                        let currentUser = rows[i]['friends_currentUser']
                        let targetUser = rows[i]['friends_targetUser']
                        let isFriend = rows[i]['friends_isFriend']


                        console.log(currentUser)
                        console.log(targetUser)
                        console.log(isFriend)
                        console.log(userId)
                        // # 접속한 userA의 경우 표현할 것
                        // # friend_a가 userA / isFriend: 0   친구 신청 중
                        // # friend_a가 userA / isFriend: 1   내 친구
                        // # friend_b가 userA / isFriend: 0   친구 수락하기 전
                        // # friend_b가 userA / isFriend: 1   내 친구

                        if (currentUser == userId && isFriend == 0) {
                            console.log("친구 신청 중")
                            temp_heml = `⛔︎${targetUser}
                    <button class="btn btn-outline-warning" onclick="deleteFriendA('${currentUser}', '${targetUser}')"> 취소</button><br>`

                        } else if ((currentUser == userId) && (isFriend == 1)) {
                            console.log("내 친구 a->b")
                            temp_heml = `👬${targetUser}
                            <button class="btn btn-outline-danger" onclick="deleteFriendA('${currentUser}', '${targetUser}')"> 절교</button><br>`

                        } else if ((targetUser == userId) && (isFriend == 1)) {
                            console.log("내 친구 b->a")
                            temp_heml = `👭${currentUser}
                            <button class="btn btn-outline-danger" onclick="deleteFriendB('${targetUser}', '${currentUser}')"> 절교</button><br>`

                        } else if (targetUser == userId && isFriend == 0) {
                            console.log("수락 대기 중")
                            temp_heml = `✓${currentUser}
                            <button class="btn btn-outline-primary" onclick="permitFriend('${currentUser}', '${targetUser}')"> 수락하기</button><br>`

                        }

                        $('#showFriend').append(temp_heml)
                    }

                }
            });

        }


                function permitFriend(currentUser, targetUser) {
            $.ajax({
                type: "POST",
                url: "/api/permitfriend",
                data: {
                    currentUser_give: currentUser,
                    targetUser_give: targetUser

                },
                success: function (response) {
                    location.reload();

                }
            });

        }

                function addFriend(user_id) {


            $.ajax({
                type: "POST",
                url: "/api/addfriend",
                data: {targetUser_give: user_id},
                success: function (response) {

                    location.reload()

                }
            });

        }

        function deleteFriendA(currentUser, targetUser) {

            $.ajax({
                type: "POST",
                url: "/api/deletefriend",
                data: {

                    currentUser_give: currentUser,
                    targetUser_give: targetUser,
                    order:"ab"
                },
                success: function (response) {
                    location.reload();
                }
            });

        }




                function deleteFriendB(targetUser, currentUser) {


            $.ajax({
                type: "POST",
                url: "/api/deletefriend",
                data: {



                    currentUser_give: targetUser,
                    targetUser_give: currentUser,
                    order:"ba"

                },
                success: function (response) {
                    location.reload();

                }
            });
}
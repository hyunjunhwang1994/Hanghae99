   <script>

             function cancelLike(post_id) {

            $.ajax({
                type: "POST",
                url: "/api/cancellike",
                data: {
                    click_give : post_id
                },
                success: function (response) {
                    window.location.reload()

                }
            });

        }


                     function clickLike(post_id) {

            $.ajax({
                type: "POST",
                url: "/api/clicklike",
                data: {
                    click_give : post_id
                },
                success: function (response) {
                    window.location.reload()
                }
            });

        }
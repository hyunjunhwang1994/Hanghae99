package com.practice.springmvcpractice.dto;


import com.practice.springmvcpractice.entity.Users;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
@NoArgsConstructor
public class UserDeleteDto {

    private String usersName;

    @Builder
    public UserDeleteDto(String usersName) {
        this.usersName = usersName;

    }


    public Users toEntity() {
        return Users.builder()
                .usersName(usersName)
                .build();

    }
}

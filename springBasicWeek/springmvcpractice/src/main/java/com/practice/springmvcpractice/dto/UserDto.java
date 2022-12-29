package com.practice.springmvcpractice.dto;


import com.practice.springmvcpractice.entity.Users;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
@NoArgsConstructor
public class UserDto {

    private String usersName;
    private String name;
    private int age;


    @Builder
    public UserDto(String usersName, String name, int age) {
        this.usersName = usersName;
        this.name = name;
        this.age = age;
    }


    public Users toEntity() {
        return Users.builder()
                .usersName(usersName)
                .name(name)
                .age(age)
                .build();

    }


}

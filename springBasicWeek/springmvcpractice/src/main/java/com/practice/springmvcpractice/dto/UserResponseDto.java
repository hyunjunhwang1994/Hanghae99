package com.practice.springmvcpractice.dto;


import com.practice.springmvcpractice.entity.Users;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@NoArgsConstructor
public class UserResponseDto {

    String result;


    public UserResponseDto(Users user) {
            this.result = "success";
    }
}

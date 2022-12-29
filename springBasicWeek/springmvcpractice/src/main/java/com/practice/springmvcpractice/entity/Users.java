package com.practice.springmvcpractice.entity;

import com.practice.springmvcpractice.dto.UserDeleteDto;
import com.practice.springmvcpractice.dto.UserDto;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import javax.persistence.*;

@Getter
@Entity
@NoArgsConstructor
public class Users {


    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;

    @Column(nullable = false)
    private String usersName;

    @Column(nullable = false)
    private String name;

    @Column(nullable = false)
    private int age;


    @Builder
    public Users(Long id, String usersName, String name, int age) {
        this.id = id;
        this.usersName = usersName;
        this.name = name;
        this.age = age;
    }

    public Users(UserDto userDto) {
        this.usersName = userDto.getUsersName();
        this.name = userDto.getName();
        this.age = userDto.getAge();

    }

    public Users(UserDeleteDto userDeleteDto) {
        this.usersName = userDeleteDto.getUsersName();
    }


}

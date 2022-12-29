package com.practice.springmvcpractice.controller;


import com.practice.springmvcpractice.dto.UserDeleteDto;
import com.practice.springmvcpractice.dto.UserDto;
import com.practice.springmvcpractice.dto.UserResponseDto;
import com.practice.springmvcpractice.service.TestService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

@RestController
@RequiredArgsConstructor
public class testController {

    private final TestService testService;


    @GetMapping("/")
    public String home() {


        return "test";
    }


    @PostMapping("/test")
    public UserResponseDto createUser(@RequestBody UserDto userDto) {

        return testService.createUser(userDto);
    }

    @DeleteMapping("/test")
    public UserResponseDto deleteUser(@RequestBody UserDeleteDto userDeleteDto) {

        return testService.deleteUser(userDeleteDto);

    }
}

package com.practice.springmvcpractice.service;


import com.practice.springmvcpractice.dto.UserDeleteDto;
import com.practice.springmvcpractice.dto.UserDto;
import com.practice.springmvcpractice.dto.UserResponseDto;
import com.practice.springmvcpractice.entity.Users;
import com.practice.springmvcpractice.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;


@Service
@RequiredArgsConstructor
public class TestService {

    private final UserRepository testRepository;
    
    
    @Transactional
    public UserResponseDto createUser(UserDto userDto){

        Users user = new Users(userDto);


        UserResponseDto userResponseDto = new UserResponseDto(user);
        if(testRepository.save(user) != null){

            userResponseDto.setResult("success");

        }else {

            userResponseDto.setResult("failed");
        }






        return userResponseDto;
    }


    @Transactional
    public UserResponseDto deleteUser(UserDeleteDto userDeleteDto) {


        Users user = new Users(userDeleteDto);
        String result = testRepository.deleteByUsersName(user.getUsersName());


        UserResponseDto userResponseDto = new UserResponseDto(user);
        if(result.equals("1")){
            userResponseDto.setResult("success");
        }else {
            userResponseDto.setResult("failed");
        }


        return userResponseDto;



    }


}


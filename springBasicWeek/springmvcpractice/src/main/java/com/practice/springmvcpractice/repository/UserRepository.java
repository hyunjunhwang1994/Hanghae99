package com.practice.springmvcpractice.repository;

import com.practice.springmvcpractice.entity.Users;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<Users, Long> {


    String deleteByUsersName(String usersName);

}

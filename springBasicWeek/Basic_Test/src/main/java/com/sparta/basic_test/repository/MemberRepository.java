package com.sparta.basic_test.repository;

import com.sparta.basic_test.entity.Member;
import org.springframework.data.jpa.repository.JpaRepository;

public interface MemberRepository extends JpaRepository<Member, Long> {

}

package com.sparta.basic_test.service;


import com.sparta.basic_test.dto.MemberResponseDto;
import com.sparta.basic_test.entity.Member;
import com.sparta.basic_test.repository.MemberRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.ArrayList;
import java.util.List;

@Service
@RequiredArgsConstructor
public class MemberService {
    private final MemberRepository memberRepository;

    @Transactional(readOnly = true)
    public MemberResponseDto findMember(Long id) {

        Member member = memberRepository.findById(id).orElseThrow(
                () -> new NullPointerException("회원 상세 조회 실패")
        );

        // Entity -> DTO
        MemberResponseDto memberResponseDto = new MemberResponseDto(member);
        return memberResponseDto;
    }


    @Transactional
    public List<MemberResponseDto> findAllMember() {

        List<Member> memberList = memberRepository.findAll();
        List<MemberResponseDto> memberResponseDtoList = new ArrayList<>();

        for (Member member : memberList) {
            MemberResponseDto postResponseDto = new MemberResponseDto(member);
            memberResponseDtoList.add(postResponseDto);
        }
        return memberResponseDtoList;

    }

}

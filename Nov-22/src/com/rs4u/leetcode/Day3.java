package com.rs4u.leetcode;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

public class Day3 {
    public int longestPalindrome(String[] words) {
        HashMap<String,Integer> differentSet = new HashMap<>();
        HashMap<String,Integer> sameMap = new HashMap<>();
        int diffCnt = 0 ;
        int maxSameCnt = 0;
        int sameCnt=0;
        for (String s: words) {
            if(differentSet.containsKey(s)){
                differentSet.put(s,differentSet.get(s)-1);
                diffCnt+=4;
                if(differentSet.get(s)==0)
                    differentSet.remove(s);
            }
            else if(s.charAt(0)==s.charAt(1)){
                Integer currentCnt = sameMap.getOrDefault(s, 0);
                maxSameCnt = Math.max(maxSameCnt , currentCnt+1);
                sameMap.put(s,currentCnt+1);
            }else{
                String s1 = Character.toString(s.charAt(1))+ s.charAt(0);
                differentSet.put(s1,differentSet.getOrDefault(s1,0)+1);
            }
        }
        boolean firstAdded = false;
        for (Map.Entry<String,Integer> entry: sameMap.entrySet()) {
            if(entry.getValue() % 2 !=0){
                sameCnt+=entry.getValue()-1;
                firstAdded = true;
            }
            else
                sameCnt+=entry.getValue();
            }
        if(firstAdded)
            sameCnt++;
        return diffCnt + sameCnt * 2;
    }


    public static void main(String[] args) {
        System.out.println(new Day3().longestPalindrome(new String[]{"lc","cl","gg"}));
        System.out.println(new Day3().longestPalindrome(new String[]{"ab","ty","yt","lc","cl","ab"}));
        System.out.println(new Day3().longestPalindrome(new String[]{"cc","ll","xx"}));
        System.out.println(new Day3().longestPalindrome(new String[]{"dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"}));
        System.out.println(new Day3().longestPalindrome(new String[]{"ab","ty","yt","lc","cl","ab","xx","xx"}));
        System.out.println(new Day3().longestPalindrome(new String[]{"ll","lb","bb","bx","xx","lx","xx","lx","ll","xb","bx","lb","bb","lb","bl","bb","bx","xl","lb","xx"}));
        System.out.println(new Day3().longestPalindrome(new String[]{"qo","fo","fq","qf","fo","ff","qq","qf","of","of","oo","of","of","qf","qf","of"}));



    }



}

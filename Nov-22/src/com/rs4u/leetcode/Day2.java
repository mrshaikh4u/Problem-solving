package com.rs4u.leetcode;

import java.util.*;
import java.util.stream.Collectors;
//
////"AACCTTGG"
////        "AATTCCGG"
////        ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]
//
//
//"AACCTTGG"
//        "AATTCCGG"
//        ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]

//"AACCGGTT"
//        "AACCGCTA"
//        ["AACCGGTA","AACCGCTA","AAACGGTA"]

public class Day2 {

    public int minMutation(String start, String end, String[] bank) {

        if(start.equals(end))
            return 0;
        int steps = 0;
        Queue<String> visits = new LinkedList<>();
        Set<String> seen = new HashSet<>();
        visits.add(start);
        seen.add(start);
        while(!visits.isEmpty()){
            int nodesInQueue = visits.size();
            for (int j = 0; j < nodesInQueue; j++) {
                String currentGene = visits.remove();
                if(currentGene.equals(end))
                    return steps;
                for (char c: new char []{'A','C','G','T'}) {
                    for (int i = 0; i < currentGene.length(); i++) {
                        String neighbor = currentGene.substring(0,i) + c + currentGene.substring(i+1);
                        if(!seen.contains(neighbor) && Arrays.asList(bank).contains(neighbor)){
                            visits.add(neighbor);
                            seen.add(neighbor);
                        }
                    }
                }
            }

            steps++;
        }
        return -1;
    }

    public static void main(String[] args) {
        System.out.println(new Day2().minMutation("AACCGGTT","AACCGGTA", new String[]{"AACCGGTA"}));
        System.out.println(new Day2().minMutation("AACCGGTT","AAACGGTA", new String[]{"AACCGGTA","AACCGCTA","AAACGGTA"}));
        System.out.println(new Day2().minMutation("AAAAACCC","AACCCCCC", new String[]{"AAAACCCC","AAACCCCC","AACCCCCC"}));
        System.out.println(new Day2().minMutation("AACCTTGG","AATTCCGG", new String[]{"AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"}));
    }
}

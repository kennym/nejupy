Feature: Source code submission to problems

    Scenario: Participant submits a source file to a Problem
        Given a Participant with username "test_participant"
        When he uploads a submission to "/competition/1/problem/1"
        Then it should be saved

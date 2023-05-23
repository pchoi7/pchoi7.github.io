--Get review table with vote count for each review
WITH annotatorsIDs AS (
    SELECT "userID"
    FROM "User"
    WHERE "User"."userEmail" IN ('nsliter@middlebury.edu', 'amcmillan@middlebury.edu', 'sychoi@middlebury.edu')
),
reviewVoteSum AS (
    SELECT "Vote"."reviewID", SUM("Vote"."voteType") AS "votes"
    FROM "Vote"
    WHERE "Vote"."votedBy" IN (SELECT * FROM annotatorsIDs)
    GROUP BY "Vote"."reviewID"
)
SELECT COALESCE(votes,0) as "votes",
       "Review"."reviewID", 
       "reviewDate", 
       "courseID", 
       "instructorID", 
       "semester", 
       "inMajorMinor", 
       "whyTake",  
       "primaryComponent",
       "tags",
       "rating", 
       "difficulty", 
       "value", 
       "hours", 
       "again", 
       "instructorEffectiveness",
       "instructorEnthusiasm",
       "instructorAccommodationLevel",
       "instructorEnjoyed",
       "instructorAgain",
       
        -- Check if user had 2 reviews within 6 months (in past) of this review
        CASE WHEN EXISTS (
            SELECT *
            FROM "Review" AS "Review2"
            WHERE "Review2"."reviewerID" = "Review"."reviewerID"
            AND "Review2"."reviewDate" <= "Review"."reviewDate"
            AND "Review2"."reviewDate" >= "Review"."reviewDate" - INTERVAL '6 months'
            AND "Review2"."reviewID" != "Review"."reviewID"
        ) THEN 1 ELSE 0 END AS "wasAuthorized",

        "content"
FROM "Review"
LEFT JOIN reviewVoteSum ON "Review"."reviewID" = reviewVoteSum."reviewID"
WHERE "Review"."reviewDate" <= timestamp '2023-04-21 18:09:01.856+00'
ORDER BY COALESCE(votes,0) desc




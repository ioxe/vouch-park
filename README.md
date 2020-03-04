# vouch-park

Code changes
1. Add holidays of next year at the end of the calendar year and delete the holidays in the past

Data refining step
1. Combine "To" into one sentence. For the scan below: "9A.M. To 11A.M." should be in one line

true [1.0] NO PARKING
true [0.5] 9A.M.
true [0.5] TO
true [1.0] 11A.M.
true [1.0] and
true [0.5] th MOT
true [0.3] Y
true [0.5] OF THE MONTH
true [1.0] STREET CLEANING
true [1.0] 10/02 SSC C&C OF S.F. 3N


2. Add "EXCEPT" as prefix to every line after you see the word

false [0.5] NO PARKING
false [0.5] TO 11AM! P.M.
false [0.5] 2nd and 4th MONDAY
false [0.5] OF THE MONTH
false [0.5] STREET CLEANING
false [0.5] 2 HOUR
false [0.5] PARKING
false [0.3] 7A.M.TO 6 P.M.
false [0.5] EXCEPT SUNDAYS

3. Combine "PAY TO", "PARK" into one line.
true true [1.0] PAY TO
true true [1.0] PARK
true true [0.5] 10am to 7pm
true true [0.5] ZONE 3
true true [1.0] PERMIT
true true [1.0] REQUIRED
true true [1.0] EVERYDAY
true true [1.0] 36 CFR 1004.12
true true [1.0] Except Federal Holidays


4. Combine "2 HOUR", "PARKING" into one string
"2 HOUR", "PARKING", "7A.M.TO 6 P.M.", "EXCEPT SUNDAYS"

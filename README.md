# vouch-park

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
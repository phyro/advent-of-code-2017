import Data.Char

solve ss =
    let zz = drop 1 ss ++ [last ss]
    in
        sum $ map (digitToInt . fst) $ filter (uncurry (==)) $ zip ss zz

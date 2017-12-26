
getDiff words =
    let 
        nums = map (read :: String -> Int) words
    in
        maximum nums - minimum nums
solve lines = sum $ map (getDiff . words) lines

main = do
    input <- getContents
    putStrLn $ show $ solve $ lines input
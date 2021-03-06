class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        result: bool = True  # assume they're isomorphic until we find a bad mapping
        mapping: dict[str, str] = {}
        s_char: str
        t_char: str
        for s_char, t_char in zip(s, t):  # iterate over both strings simultaneously
            if s_char not in mapping and t_char not in mapping.values():  # if both s and t are free, map them
                mapping[s_char] = t_char
            elif s_char not in mapping or mapping[s_char] != t_char:  # if they aren't, then s must map to t
                result = False  # s does not map to t
                break  # we can't make this mapping because s or t (or both) are unavailable, so we're done
        return result

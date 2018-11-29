import java.io.IOException;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class Main {

	private static Map<String, Set<String>> wordsCombination = new HashMap<>();

	public static void main(String[] args) throws IOException {

		String[] input = { "crates", "car", "cats", "crate", "rate", "at", "ate", "tea", "rat", "a" };

//		String[] input = { "b", "bcad", "bca", "bad", "bd" };

//		String[] input = { "word", "anotherword", "yetanotherword" };

		wordsCombination = getWordsCombinations(input);
		System.out.println(wordsCombination);
		Set<String> result = new LinkedHashSet<>();
		result = getLongestGame();
		if (result.isEmpty()) {
			result.add(wordsCombination.keySet().iterator().next());
		}
		System.out.println(result.size());
		System.out.println(result);
	}

	private static Map<String, Set<String>> getWordsCombinations(String[] input) throws IOException {
		Map<String, Set<String>> result = new HashMap<String, Set<String>>();
		List<String> lines = Arrays.asList(input);
		for (String line : lines) {
			String word1 = line.trim();
			if (!result.containsKey(word1)) {
				result.put(word1, new HashSet<>());
			}
			Map<String, String> opt = new HashMap<>();
			combine(opt, word1, new StringBuilder(), 0);
			for (String word : opt.values()) {
				if (lines.contains(word) && word1.length() - 1 == word.length() && !word.equals(word1)) {
					result.get(word1).add(word);
				}
			}
		}
		return result;
	}
6
	private static void combine(Map<String, String> opt, String inputstring, StringBuilder output, int start) {
		for (int i = start; i < inputstring.length(); ++i) {
			output.append(inputstring.charAt(i));
			opt.put(output.toString(), output.toString());
			if (i < inputstring.length())
				combine(opt, inputstring, output, i + 1); 
			output.setLength(output.length() - 1);
		}
	}

	private static Set<String> getLongestGame() {
		Set<String> result = new HashSet<>();
		for (String key : wordsCombination.keySet()) {
			if (!wordsCombination.get(key).isEmpty()) {
				fillNextWord(result, key);
			}
		}
		return result;
	}

	private static void fillNextWord(Set<String> result, String word) {
		boolean hasSimilarWord = false;
		for (String existingWord : result) {
			if (existingWord.length() == word.length()) {
				hasSimilarWord = true;
				break;
			}
		}
		if (!hasSimilarWord) {
			result.add(word);
		}
		if (!wordsCombination.get(word).isEmpty()) {
			fillNextWord(result, wordsCombination.get(word).iterator().next());
		}
	}
}

'''

'''

from faker.providers import BaseProvider


class ElevatorPitchProvider(BaseProvider):

    _superlatives = [
        "edge-of-your-seat",
        "keenly observed",
        "lyrical",
        "profound",
        "erotic",
        "inspiring",
        "razor-sharp",
        "heartrending",
        "dream-like",
        "darkly comic",
        "uncompromising",
        "courageous",
        "compulsively readable",
        "unflinching",
        "fiercely honest",
        "richly drawn",
        "unforgettable",
        "riveting",
        "high-voltage",
        "psycho-sexual",
        "riotously funny",
        "passionate",
        "surreal",
        "dystopian",
        "hysterical",
        "meditative",
    ]

    _genres = [
        "thriller",
        "meditation",
        "coming of age story",
        "family drama",
        "war epic",
        "episotolary novel",
        "romance",
        "tragedy",
        "story",
        "tour de force",
        "comedy",
        "noir",
        "instant classic",
        "fairy tale",
        "autobiographical novel",
        "romp",
        "fictional memoir",
        "trilogy",
        "detective novel",
        "page-turner",
        "tragicomedy",
        "murder mystery",
        "novel in stories",
        "historical novel",
        "graphic novel",
        "saga"
    ]

    _protagonist_descriptions = [
        "depressed",
        "wealthy",
        "doomed",
        "exuberant",
        "agoraphobic",
        "maladjusted",
        "misanthropic",
        "alcoholic",
        "young",
        "philosophical",
        "hopelessly romantic",
        "hyper-sexual",
        "precocious",
        "unlucky",
        "quixotic",
        "desperate",
        "refugee",
        "dissatisfied",
        "bored",
        "morally compromised",
        "lovesick",
        "drug-addled",
        "jilted",
        "vengeful",
        "overbearing",
        "closeted",
    ]

    _protagonists = [
        "man",
        "orphan",
        "daughter",
        "mother",
        "adoloscent",
        "soldier",
        "student",
        "widow",
        "woman",
        "professor",
        "divorcee",
        "adventurer",
        "extended family",
        "child",
        "mistress",
        "dictator",
        "vampire",
        "ghost",
        "starship captain",
        "doctor",
        "writer",
        "private investigator",
        "couple",
        "coven",
        "murder detective",
        "octogenarian",
    ]

    _commitments = [
        "adventure",
        "commitment",
        "desire",
        "devotion",
        "dream",
        "effort",
        "strategy",
        "pains",
        "failure",
        "inability",
        "journey",
        "mission",
        "not-so-secret desire",
        "quest",
        "endeavour",
        "secret longing",
        "struggle",
        "vacation",
        "wish",
        "expedition",
        "plan",
        "scheme",
        "resolve",
        "project",
        "promise",
        "battle"
    ]

    _verbs = [
        "re-awaken",
        "come to grips with",
        "grapple with",
        "understand",
        "explore",
        "accept",
        "overcome",
        "avenge",
        "pursue",
        "defend",
        "undertake",
        "discover",
        "contemplate",
        "transcend",
        "withdraw from",
        "avoid",
        "betray",
        "circumvent",
        "confront",
        "expose",
        "give up",
        "investigate",
        "navigate",
        "reconnect with",
        "embrace",
        "reconcile to"
    ]

    _conflicts = [
        "fear of spiders",
        "adoption",
        "traumatic childhood",
        "mother's death",
        "sexless marriage",
        "Oedipal complex",
        "feminism",
        "religious upbringing",
        "political apathy",
        "biological clock",
        "ugly divorce",
        "write's block",
        "toxic friendships",
        "eating disorder",
        "own birth",
        "cancer",
        "23andMe results",
        "privilege",
        "untimely death",
        "social media addiction",
        "spiritual evolutin",
        "secret second family",
        "sexual awakening",
        "Amazon reviews",
        "father's murder",
        "disinheritance"
    ]

    _pronouns = ['his', 'her', 'their']

    @property
    def superlative(self):
        return self.random_element(self._superlatives)

    @property
    def genre(self):
        return self.random_element(self._genres)

    @property
    def protagonist_description(self):
        return self.random_element(self._protagonist_descriptions)

    @property
    def protagonist(self):
        return self.random_element(self._protagonists)

    @property
    def commitment(self):
        return self.random_element(self._commitments)

    @property
    def verb(self):
        return self.random_element(self._verbs)

    @property
    def conflict(self):
        return self.random_element(self._conflicts)

    @property
    def _pronoun(self):
        return self.random_element(self._pronouns)

    def _determiner_for(self, word):
        return 'an' if word[0].lower() in 'aeiou' else 'a'

    def elevator_pitch(self):
        '''
        '''
        superlative = self.superlative
        protagonist_description = self.protagonist_description

        return ' '.join([self._determiner_for(superlative).capitalize(),
                         superlative,
                         self.genre,
                         'about',
                         self._determiner_for(protagonist_description),
                         protagonist_description,
                         self.protagonist + "'s",
                         self.commitment,
                         'to',
                         self.verb,
                         self._pronoun,
                         self.conflict]) + '.'

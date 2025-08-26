import openai
from scenario import All_Scenario

class OpenAIConfig:
    def __init__(self, api_key: str = "api-key", model: str = "gpt-4o-mini"):
        """
        Initializes the OpenAI API configuration with the given API key and model.
        """
        self.api_key = api_key
        self.model = model
        openai.api_key = self.api_key
        self.conversation_history = [{"role": "system", "content": "You are a helpful wellness coach."}]

    def get_response(self, prompt: str, history: list, context: str = None) -> str:
        """
        Sends a prompt to the OpenAI API and returns the response text.
        Maintains conversation history for context.
        """
        try:

            system_prompt = f"""
            You are a calm, empathetic, and friendly wellness coach specializing in women's health and well-being. Your role is to guide users through physical, emotional, and lifestyle challenges with short, supportive, and thoughtful responses.
            Your tone should be warm, non-judgmental, and empowering. You respond only to health and wellness-related topics (like women's cycle, phase etc.). If a user provides irrelevant, inappropriate, or unclear input, gently redirect them or ask for clarification. You do not speculate or respond to topics outside of wellness.
            Below are the scenarios to follow when interacting with users:
            1. {All_Scenario.scenario1}
            2. {All_Scenario.scenario2}
            3. {All_Scenario.scenario3}
            4. {All_Scenario.scenario4}
            5. {All_Scenario.scenario5}
            6. {All_Scenario.secnario6}
            7. {All_Scenario.scenario7}
            8. {All_Scenario.scenario8}
            9. {All_Scenario.scenario9}
            10. {All_Scenario.scenario10}
            11. {All_Scenario.scenario11}
            12. {All_Scenario.scenario12}
            13. {All_Scenario.scenario13}
            14. {All_Scenario.scenario14}
            15. {All_Scenario.scenario15}
            16. {All_Scenario.scenario16}
            17. {All_Scenario.scenario17}
            18. {All_Scenario.scenario18}
            19. {All_Scenario.scenario19}
            20. {All_Scenario.scenario20}
            21. {All_Scenario.scenario21}
            22. {All_Scenario.scenario22}
            23. {All_Scenario.scenario23}
            24. {All_Scenario.scenario24}
            25. {All_Scenario.scenario25}
            26. {All_Scenario.scenario26}
            27. {All_Scenario.scenario27}
            28. {All_Scenario.scenario28}
            29. {All_Scenario.scenario29}
            30. {All_Scenario.scenario30}
            31. {All_Scenario.scenario31}
            32. {All_Scenario.scenario32}
            33. {All_Scenario.scenario33}
            34. {All_Scenario.scenario34}
            35. {All_Scenario.scenario35}
            36. {All_Scenario.scenario36}
            37. {All_Scenario.scenario37}
            38. {All_Scenario.scenario38}
            39. {All_Scenario.scenario39}
            40. {All_Scenario.scenario40}
            41. {All_Scenario.scenario41}
            42. {All_Scenario.scenario42}
            43. {All_Scenario.scenario43}
            44. {All_Scenario.scenario44}
            45. {All_Scenario.scenario45}
            46. {All_Scenario.scenario46}
            47. {All_Scenario.scenario47}
            48. {All_Scenario.scenario48}
            49. {All_Scenario.scenario49}
            50. {All_Scenario.scenario50}
            51. {All_Scenario.scenario51}
            52. {All_Scenario.scenario52}
            53. {All_Scenario.scenario53}
            54. {All_Scenario.scenario54}
            55. {All_Scenario.scenario55}
            56. {All_Scenario.scenario56}
            If a user input does not match any predefined scenario, confidently respond using your understanding of wellness principles and the patterns learned from the provided scenarios. Use your best judgment to guide the user with empathy and clarity, as if the scenario were already known.
            If no scenario applies, respond as a general wellness coach. Always prioritize clarity, empathy, and encouragement. If the user seems confused or misinformed, kindly help them reframe or correct their input.
            Always maintain a supportive tone, but adapt your emotional energy to match the user's mood.
            Your goal is to help women feel heard, supported, and informed about their health journey.
            """

            full_system_prompt = system_prompt
            if context:
                full_system_prompt += f"\n\nHere is additional context from the wellness guide:\n{context}"

            # Build API history separately
            api_history = [{"role": "system", "content": full_system_prompt}] + history + [{"role": "user", "content": prompt}]

            response = openai.ChatCompletion.create(
                model=self.model,
                messages=api_history
            )

            reply = response.choices[0].message['content']

            # Append only user and assistant messages to session history
            history.append({"role": "user", "content": prompt})
            history.append({"role": "assistant", "content": reply})

            return reply


        except Exception as e:
            print(f"Error communicating with OpenAI API: {e}")
            return "Sorry, I couldn't process your request at the moment. Please try again later."
        

    def get_history(self):
        return self.conversation_history

    def generate_insight(self, cycle: str, phase: str, context: str):
        """
        Generates a tailored FENYX insight based on the user's cycle and phase.
        
        :param cycle: The user's cycle (e.g., 'Yes' for regular cycle).
        :param phase: The selected phase (e.g., 'Luteal', 'Follicular').
        :param context: Optional context (e.g., PDF content) for personalized insights.
        :return: The generated FENYX insight.
        """
        try:
            prompt = f"Generate a concise, informative insight for a user with cycle '{cycle}' and phase '{phase}', without offering suggestions, questions, or personal advice. Just provide a clear insight message."

            response = self.get_response(prompt, history=[], context=context)

            return response
        except Exception as e:
            print(f"Error generating insight: {e}")
            return "Sorry, I couldn't generate your insight at the moment. Please try again later."
        

    def get_goal(self, cycle: str, phase: str, context: str):
        """
        Generates a goal-oriented response based on the user's cycle and phase. Focuses on describing the goal
        of the phase without additional food or supplement suggestions.
        
        :param cycle: The user's cycle (e.g., 'Yes' for regular cycle).
        :param phase: The selected phase (e.g., 'Follicular', 'Luteal').
        :param context: Optional context (e.g., PDF content) for personalized responses.
        :return: The generated goal-oriented response.
        """
        try:
            prompt = f"Not ask any type of question or warm message, Generate a goal-based, descriptive response for a user in the '{phase}' phase with cycle '{cycle}', emphasizing the key goals of this phase, such as hormonal changes, energy focus, or mental clarity. Avoid any food suggestions, supplements, or questions, and do not suggest any specific actions unless they directly relate to the goal of the phase."

            response = self.get_response(prompt, history=[], context=context)

            return response
        except Exception as e:
            print(f"Error generating goal response: {e}")
            return "Sorry, I couldn't process your goal at the moment. Please try again later."
        

    def get_food(self, cycle: str, phase: str, context: str):
        """
        Generates food suggestions based on the user's cycle and phase.
        :param cycle: The user's cycle (e.g., 'Yes' for regular cycle).
        :param phase: The selected phase (e.g., 'Follicular', 'Luteal').
        :param context: Optional context (e.g., PDF content) for personalized food suggestions.
        :return: The generated food suggestions.
        """
        try:
            prompt = f"Generate a concise, narrative-style food suggestion for a user in the '{phase}' phase with cycle '{cycle}'. Describe the most beneficial foods for this phase. Also, mention which foods to avoid, with a short rationale. Keep the response focused, natural, and to the point. And remember that do not ask any question or specific actions unless they directly relate to the food suggestions."
            
            response = self.get_response(prompt, history=[], context=context)
            return response
        except Exception as e:
            print(f"Error generating food suggestions: {e}")
            return "Sorry, I couldn't provide food suggestions at the moment. Please try again later."
        

    def get_supplement(self, cycle: str, phase: str, context: str):
        """
        Generates supplement suggestions based on the user's cycle and phase.
        :param cycle: The user's cycle (e.g., 'Yes' for regular cycle).
        :param phase: The selected phase (e.g., 'Follicular', 'Luteal').
        :param context: Optional context (e.g., PDF content) for personalized supplement suggestions.
        :return: The generated supplement suggestions.
        """
        try:
            prompt = f"Generate a concise, narrative-style supplement suggestions for a user in the '{phase}' phase with cycle '{cycle}'. Focus on supplements based on pdf, that support hormonal balance, energy levels, and overall well-being during this phase and avoid any content which is not in pdf."
            
            response = self.get_response(prompt, history=[], context=context)
            return response
        except Exception as e:
            print(f"Error generating supplement suggestions: {e}")
            return "Sorry, I couldn't provide supplement suggestions at the moment. Please try again later."
import openai

class OpenAIConfig:
    def __init__(self, api_key: str = "api-key", model: str = "gpt-4o-mini"):
        """
        Initializes the OpenAI API configuration with the given API key and model.
        """
        self.api_key = api_key
        self.model = model
        openai.api_key = self.api_key

    def get_response(self, prompt: str, temperature: float = 0.7, max_tokens: int = 150, context: str = None):
        """
        Sends a request to OpenAI's API and returns the response, incorporating optional context (such as PDF content).
        
        :param prompt: The input prompt for the model.
        :param temperature: Sampling temperature (default is 0.7).
        :param max_tokens: Maximum number of tokens to generate (default is 150).
        :param context: Optional context (e.g., PDF content) to provide for better responses.
        :return: The generated AI response.
        """
        try:
            system_prompt = """
            You are a calm, empathetic, and friendly wellness coach. Your responses should be short, thoughtful, and supportive. Your goal is to help users feel empowered and informed about their health, fitness, and emotional well-being.

            You should generate a response based on the scenarios and guidance from the provided PDF content. After each follow-up question, make sure to continue the conversation naturally, integrating the user's latest answer into the response.

            - If the user has provided an answer (e.g., "Avoiding"), acknowledge their response and avoid repeating the same question.
            - Ask for clarification only when the user's response is unclear or incomplete, using empathetic language.
            - Provide a short suggestion or action for the user to take after completing each follow-up question.

            Remember to guide the user with gentle and supportive suggestions. The tone should remain calm and empathetic, with responses that reflect the user’s needs, progress, and current situation.
            """
            
            
            user_prompt = f"User's question: {prompt}"
            if context:
                user_prompt += f"\n\nHere is some relevant information from the wellness guide:\n{context}"

            final_prompt = f"{system_prompt}\n{user_prompt}"

            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": final_prompt}],
                temperature=temperature,
                max_tokens=max_tokens
            )

            return response['choices'][0]['message']['content']
        except Exception as e:
            print(f"Error communicating with OpenAI API: {e}")
            return "Sorry, I couldn't process your request at the moment. Please try again later."
        


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

            response = self.get_response(prompt, context=context)

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

            response = self.get_response(prompt, context=context)

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
            
            response = self.get_response(prompt, context=context)
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
            
            response = self.get_response(prompt, context=context)
            return response
        except Exception as e:
            print(f"Error generating supplement suggestions: {e}")
            return "Sorry, I couldn't provide supplement suggestions at the moment. Please try again later."
        

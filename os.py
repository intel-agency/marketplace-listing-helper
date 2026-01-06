from team import marketplace_team
from agents import fb_agent #, cl_agent, offerup_agent



def main():
    print("Hello from jobhelperagents!")
    # Test run
    # job_helper_team.print_response(
    #     "Find me 10 Senior Software Engineer, backend or embedded, roles in Seattle, WA", stream=True
    # )

agent_os = AgentOS(
    id="my-first-os",
    description="My first AgentOS",
    agents=[fb_agent],
)

app = agent_os.get_app()

if __name__ == "__main__":
    # Default port is 7777; change with port=...
    agent_os.serve(app="my_os:app", reload=True)


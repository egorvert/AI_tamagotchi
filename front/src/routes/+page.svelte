<script>
	let narrator = "Welcome to Tamagotchi Game";
	let pet = "Jeffrey";
	let imageUrl = "";
	let prompt = "";

	async function generateImage() {
		try {
			const response = await fetch(
				`http://localhost:8000/generate-image?prompt=${encodeURIComponent(prompt)}`
			);
			if (response.ok) {
				const blob = await response.blob();
				imageUrl = URL.createObjectURL(blob);
			}
		} catch (error) {
			console.error("Error generating image:", error);
		}
	}
</script>

<svelte:head>
	<link
		href="https://fonts.googleapis.com/css2?family=Doto:wght@100..900&display=swap"
		rel="stylesheet"
	/>
</svelte:head>

<div class="container">
	<h1>{pet}</h1>
	<div class="image-row">
		<img
			src="/cat_placeholder.jpg"
			alt="Cat placeholder"
			width="500"
			height="500"
		/>
	</div>

	<div class="textbox-container">
		<p>> {narrator}</p>
	</div>

	<div class="button-row">
		<button>Button 1</button>
		<button>Button 2</button>
		<button>Button 3</button>
	</div>
</div>

<input bind:value={prompt} placeholder="Enter prompt" />
<button on:click={generateImage}>Generate Image</button>

{#if imageUrl}
	<img src={imageUrl} />
{/if}

<style>
	:global(body) {
		margin: 0;
		padding: 0;
		font-family: "Doto", sans-serif;
		font-optical-sizing: auto;
		background-color: #1b1b1b;
		color: white;
	}

	* {
		box-sizing: border-box;
	}

	.container {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		height: 100vh;
		gap: 2rem;
		box-sizing: border-box;
		padding: 1rem;
	}

	.image-row {
		display: flex;
		justify-content: center;
	}

	.button-row {
		display: flex;
		gap: 1rem;
		justify-content: center;
	}

	.textbox-container {
		display: flex;
		align-items: center;
		justify-content: center;
		border: 1px solid #fff;
		width: 60%;
	}

	h1 {
		text-align: center;
	}

	p {
		font-size: 18px;
	}

	img {
		max-width: 100%;
		max-height: calc(70vh - 2rem); /* Ensure image doesn't cause overflow */
		height: auto;
		object-fit: contain;
	}

	button {
		padding: 0.5rem 1rem;
		border: 1px solid #ccc;
		border-radius: 4px;
		background-color: #f9f9f9;
		cursor: pointer;
	}

	button:hover {
		background-color: #eee;
	}
</style>

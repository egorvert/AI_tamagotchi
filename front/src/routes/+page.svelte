<div class="container">
	<div class="image-row">
		<img
			src="/cat_placeholder.jpg"
			alt="Cat placeholder"
			width="500"
			height="500"
		/>
	</div>

	<div class="button-row">
		<button>Button 1</button>
		<button>Button 2</button>
		<button>Button 3</button>
	</div>
</div>

<style>
	:global(body) {
		margin: 0;
		padding: 0;
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

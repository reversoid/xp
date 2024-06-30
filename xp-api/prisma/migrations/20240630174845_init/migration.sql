-- CreateTable
CREATE TABLE "users" (
    "id" VARCHAR(10) NOT NULL,
    "tg_id" BIGINT NOT NULL,
    "tg_username" VARCHAR(32) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "users_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "subscriptions" (
    "tg_username" VARCHAR(32) NOT NULL,
    "user_id" VARCHAR(10),
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "until" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "subscriptions_pkey" PRIMARY KEY ("tg_username")
);

-- CreateTable
CREATE TABLE "observations" (
    "_id" SERIAL NOT NULL,
    "id" VARCHAR(10) NOT NULL,
    "user_id" VARCHAR(10) NOT NULL,
    "tg_text" TEXT,
    "tg_photo_id" VARCHAR(255),
    "tg_video_id" VARCHAR(255),
    "tg_voice_id" VARCHAR(255),
    "tg_document_id" VARCHAR(255),
    "tg_video_note_id" VARCHAR(255),
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "observations_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "observation_views" (
    "observation_id" VARCHAR(10) NOT NULL,
    "user_id" VARCHAR(10) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- CreateTable
CREATE TABLE "experiments" (
    "_id" SERIAL NOT NULL,
    "id" VARCHAR(10) NOT NULL,
    "user_id" VARCHAR(10) NOT NULL,
    "tg_text" TEXT,
    "tg_photo_id" VARCHAR(255),
    "tg_video_id" VARCHAR(255),
    "tg_voice_id" VARCHAR(255),
    "tg_document_id" VARCHAR(255),
    "tg_video_note_id" VARCHAR(255),
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "complete_by" TIMESTAMPTZ NOT NULL,
    "completed_at" TIMESTAMPTZ,
    "canceled_at" TIMESTAMPTZ,

    CONSTRAINT "experiments_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "experiment_views" (
    "experiment_id" VARCHAR(10) NOT NULL,
    "user_id" VARCHAR(10) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- CreateTable
CREATE TABLE "tg_media_group_items" (
    "id" SERIAL NOT NULL,
    "tg_audio_id" TEXT,
    "tg_document_id" TEXT,
    "tg_photo_id" TEXT,
    "tg_video_id" TEXT,
    "experiment_id" VARCHAR(10),
    "observation_id" VARCHAR(10),

    CONSTRAINT "tg_media_group_items_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "tg_geos" (
    "id" SERIAL NOT NULL,
    "longitude" DOUBLE PRECISION NOT NULL,
    "latitude" DOUBLE PRECISION NOT NULL,
    "horizontal_accuracy" INTEGER,
    "observation_id" VARCHAR(10),
    "experiment_id" VARCHAR(10),

    CONSTRAINT "tg_geos_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "users_tg_id_key" ON "users"("tg_id");

-- CreateIndex
CREATE UNIQUE INDEX "subscriptions_user_id_key" ON "subscriptions"("user_id");

-- CreateIndex
CREATE UNIQUE INDEX "observations__id_key" ON "observations"("_id");

-- CreateIndex
CREATE UNIQUE INDEX "observation_views_observation_id_user_id_key" ON "observation_views"("observation_id", "user_id");

-- CreateIndex
CREATE UNIQUE INDEX "experiments__id_key" ON "experiments"("_id");

-- CreateIndex
CREATE UNIQUE INDEX "experiment_views_experiment_id_user_id_key" ON "experiment_views"("experiment_id", "user_id");

-- CreateIndex
CREATE UNIQUE INDEX "tg_geos_observation_id_key" ON "tg_geos"("observation_id");

-- CreateIndex
CREATE UNIQUE INDEX "tg_geos_experiment_id_key" ON "tg_geos"("experiment_id");

-- AddForeignKey
ALTER TABLE "subscriptions" ADD CONSTRAINT "subscriptions_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "users"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "observations" ADD CONSTRAINT "observations_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "users"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "observation_views" ADD CONSTRAINT "observation_views_observation_id_fkey" FOREIGN KEY ("observation_id") REFERENCES "observations"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "experiments" ADD CONSTRAINT "experiments_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "users"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "experiment_views" ADD CONSTRAINT "experiment_views_experiment_id_fkey" FOREIGN KEY ("experiment_id") REFERENCES "experiments"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "tg_media_group_items" ADD CONSTRAINT "tg_media_group_items_observation_id_fkey" FOREIGN KEY ("observation_id") REFERENCES "observations"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "tg_media_group_items" ADD CONSTRAINT "tg_media_group_items_experiment_id_fkey" FOREIGN KEY ("experiment_id") REFERENCES "experiments"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "tg_geos" ADD CONSTRAINT "tg_geos_observation_id_fkey" FOREIGN KEY ("observation_id") REFERENCES "observations"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "tg_geos" ADD CONSTRAINT "tg_geos_experiment_id_fkey" FOREIGN KEY ("experiment_id") REFERENCES "experiments"("id") ON DELETE SET NULL ON UPDATE CASCADE;
